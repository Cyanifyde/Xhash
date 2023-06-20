import math

class Hash:
    
    def __init__(self,hash_length=256):
        self.hash_length = hash_length
        self.coords = []
        self.output_coords = []
        self.last_hash=""

    def hash(self, string: str, salt: str):
        string += salt
        generated_int = 0
        hash_value = ""
        
        while len(hash_value.encode('utf-8')) < self.hash_length:
            string += str(generated_int)
            self.coords.clear()
            self.output_coords.clear()
            self.generate_lines(string, self.coords)
            rotated_string = string[len(string) // 4:] + string[:len(string) // 4]
            self.generate_lines(rotated_string, self.output_coords)
            all_intersections = 0
            for line in self.output_coords:
                intersections = self.count_intersections(line, self.coords)
                angles = self.intersection_angles(line, self.coords)
                all_intersections += int((intersections + sum(angles)) * 1e8)
            generated_int = all_intersections
            hash_value += str(generated_int)

        while len(hash_value)>self.hash_length:
            hash_value=str(self.trim(hash_value))
        self.last_hash=hash_value
        self.coords.clear()
        self.output_coords.clear()
        return hash_value.encode('utf-8')

    def trim(self, string):
        remaining=string
        value=0
        while len(remaining)>0:
            if len(remaining)-self.hash_length<0:
                value+=int(remaining)
                remaining=""
            else:
                half1 = remaining[:self.hash_length]
                remaining = remaining[self.hash_length:]
                value+=int(half1)
        return value
        
    def generate_lines(self, string, coords):
        string = string.ljust(((len(string) + 3) // 4) * 4, 'a')
        for i in range(0, len(string), 4):
            coords.append(self.string_to_coordinates(string[i:i + 4]))

    def string_to_coordinates(self, s):
        return [(ord(s[0]), ord(s[1])), (ord(s[2]), ord(s[3]))]

    def line_parameters(self, line):
        (x1, y1), (x2, y2) = line
        if x1 != x2:
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
        else:
            slope = None
            intercept = None
        return slope, intercept

    def line_intersection(self, line1, line2):
        m1, c1 = self.line_parameters(line1)
        m2, c2 = self.line_parameters(line2)
        if m1 == m2:
            return None
        elif m1 is None:
            x = line1[0][0]
            y = m2 * x + c2
        elif m2 is None:
            x = line2[0][0]
            y = m1 * x + c1
        else:
            x = (c2 - c1) / (m1 - m2)
            y = m1 * x + c1
        return [x, y]

    def count_intersections(self, input_line, line_list):
        return sum(self.line_intersection(input_line, line) is not None for line in line_list)

    def intersection_angles(self, input_line, line_list):
        m1, _ = self.line_parameters(input_line)
        if m1 is None:
            return [0]*len(line_list)
        else:
            angles = []
            for line in line_list:
                m2, _ = self.line_parameters(line)
                if m2 is not None:
                    if m1 * m2 == -1:
                        angle = math.pi / 2
                    else:
                        angle = math.atan(abs((m2 - m1) / (1 + m1 * m2)))
                    angles.append(angle)
                else:
                    angles.append(0)
            return angles
    
