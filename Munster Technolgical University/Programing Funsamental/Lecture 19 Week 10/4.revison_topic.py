# Author : Mofazzal Hossain
# Description : revision topic

number = 1256.8953

# {alignment, field_width, comma, precision, datatype}

example = f"Within this string, I can embed the value {number:^20,.0f}end."  # < ^ >
# f- float , d - integer , s - string , %-percentage , e- scientific notation (round nearest decimal position )

print(example)