from expression_parsing.notation import Notation

notation = Notation()

infix = '(a + b) ∗ (c + d)'
print('infix: ', infix)
postfix = notation.infix_postfix(infix)
print('postfix: ', postfix)
prefix = notation.postfix_prefix(postfix)
print('prefix: ', prefix)
infix_prim = notation.postfix_infix(postfix)
print('infix_prim: ', infix_prim)

postfix_prim = notation.prefix_postfix(prefix)
print('postfix_prim: ', postfix_prim)
