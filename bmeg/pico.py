import pico_pb2 as schema

# (fn [x]
#   (reduce
#    (fn [a b] (+ a b))
#    0 (vals (get x "count"))))

def sym(symbol):
    e = schema.Expression()
    e.atom.binding = symbol
    return e

def s(value):
    e = schema.Expression()
    e.atom.string = value
    return e

def n(value):
    e = schema.Expression()
    e.atom.number = float(value)
    return e

nil = schema.Nil()
nil.nil = True

def l(*items):
    e = schema.Expression()
    e.list.items.extend(items)
    return e

def fn(arguments, body):
    e = schema.Expression()
    e.fn.arguments.extend(arguments)
    e.fn.body.CopyFrom(body)
    return e

add = fn(['a', 'b'],
         l(sym('+'),
           sym('a'),
           sym('b')))

fold = fn(['x'],
          l(sym('reduce'),
            add,
            n(0),
            l(sym('vals'),
              l(sym('get'),
                sym('x'),
                s('count')))))

print fold
