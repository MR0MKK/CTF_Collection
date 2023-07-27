import brainfuck
hello = brainfuck.to_function("""
    ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>
    .>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
    """)
hello()
# 'Hello World!\n'