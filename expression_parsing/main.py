from expression_parsing.notation import Notation

notation = Notation()

# in1 = '3+4*2/(1-5)^2'
# pre1 = notation.in_to_pre(in1)
# print(pre1)
# in1_prim = notation.pre_to_in(pre1)
# print(in1_prim, in1)

# notation.in_to_pre('12 + a * (b * c + d / e)')

notation.pre_to_post('+ A B')

