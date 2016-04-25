'''Property will convert attribute access like a.x into method access like a.m()
   They only work with new-style classes.

'''

class InvoiceLineItem(object):

    def __init__(self, inv_no, line_no, cat_no, unit_price, quantity):
        self.inv_no = inv_no
        self.line_no = line_no
        self.cat_no = cat_no
        self.unit_price = unit_price
        self.quantity = quantity

    @property                                   # total = property(total)
    def total(self):
        return self.unit_price * self.quantity

class Invoice(object):

    def __init__(self, customer, inv_no, order):
        self.customer = customer
        self.inv_no = inv_no
        line_items = []
        for line_no, (quantity, cat_no) in enumerate(order, 1):
             unit_price = price_sheet[cat_no]
             line_item = InvoiceLineItem(inv_no, line_no, cat_no, unit_price, quantity)
             line_items.append(line_item)
        self.line_items = line_items

    @property
    def total(self):
        return sum(line_item.total for line_item in self.line_items)

price_sheet = dict(
    CAT1234 = 28.17,
    CAT4300 = 64.12,
    CAT5918 = 34.14,
    CAT8701 = 44.73,
    CAT9817 = 42.56,
)

invoice = Invoice('Cisco', 'INV1040', [(15, 'CAT5918'), (20, 'CAT8701')])
print invoice.total

