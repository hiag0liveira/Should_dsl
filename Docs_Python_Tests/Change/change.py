from should_dsl import should, should_not

class Box(object):
    def __init__(self):
        self.items = []
    def add_items(self, *items):
        for item in items:
            self.items.append(item)
    def item_count(self):
        return len(self.items)
    def clear(self):
        self.items = []

box = Box()

def test_item_count_lambda_passed():
    # wrong:
        # (box.add_items, 1) |should| change(box.items)
        # Traceback (most recent call last):
        # ...
        # TypeError: parameter passed to change must be a callable or a iterable having a callable as its first element
    
    #right:
        (lambda: box.add_items(1)) |should| change(box.item_count)


def test_item_count_lambda_failed():
    (lambda: box.add_items(1)) |should_not| change(box.item_count)
    #Traceback (most recent call last):
    #...
    #ShouldNotSatisfied: should not have changed, but did change from 1 to 2


def test_item_count_lambda_failed2():    
    (lambda: 0) |should| change(box.item_count)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed, but is still 2


def test_item_count_lambda_passed2():
     (lambda: 0) |should_not| change(box.item_count)


def test_item_count_passed():
    (box.add_items, 1) |should| change(box.item_count)


def test_item_count_by_lambda_passed():   
    # wrong:
        # (box.add_items, 1) |should| change(box.items)
        # Traceback (most recent call last):
        #     ...
        # TypeError: parameter passed to change must be a callable or a iterable having a callable as its first element

        #(1, box.add_items) |should| change(box.item_count)
        # Traceback (most recent call last):
        #     ...
        # TypeError: parameter passed to change must be a callable or a iterable having a callable as its first element
    
    # right:
        (lambda: box.add_items(1)) |should| change(box.item_count).by(1)


def test_item_count_by_lambda_failed():   
    (lambda: box.add_items(1)) |should| change(box.item_count).by(2)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed by 2, but was changed by 1


def test_item_count_by_lambda_passed2():    
    (lambda: 1) |should| change(box.item_count).by(0)


def test_item_count_by_char_passed():    
    box.clear()
    box.add_items('a')
    box.clear |should| change(box.item_count).by(-1)


def test_item_count_by_at_least_passed():  
    (box.add_items, 1, 2, 3) |should| change(box.item_count).by_at_least(3)


def test_item_count_by_at_least_passed2():
    (box.add_items, 1, 2, 3) |should| change(box.item_count).by_at_least(2)


def ttest_item_count_by_at_least_failed(): 
    (box.add_items, 1, 2, 3) |should| change(box.item_count).by_at_least(4)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed by at least 4, but was changed by 3


def test_item_count_by_at_most_passed():   
    (box.add_items, 1, 2, 3) |should| change(box.item_count).by_at_most(3)


def test_item_count_by_at_most_passed2():    
    (box.add_items, 1, 2, 3) |should| change(box.item_count).by_at_most(4)


def test_item_count_by_at_most_failed():   
    (box.add_items, 1, 2, 3) |should| change(box.item_count).by_at_most(2)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed by at most 2, but was changed by 3


def test_item_count_from_to_passed(): 
    box.clear()
    (box.add_items, 3, 5, 7) |should| change(box.item_count).from_(0).to(3)


def test_item_count_from_to_passed2():    
    box.clear |should| change(box.item_count).from_(3).to(0)


def test_item_count_from_to_failed():   
    (box.add_items, 3, 5, 7) |should| change(box.item_count).from_(0).to(2)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed from 0 to 2, but was changed from 0 to 3


def test_item_count_from_to_failed2():    
    box.clear |should_not| change(box.item_count).from_(3).to(0)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should not have changed from 3 to 0


def test_item_count_to_passed():
    box.add_items(1)
    box.clear |should| change(box.item_count).to(0)


def test_item_count_to_passed():    
    (box.add_items, 3, 4) |should_not| change(box.item_count).to(3)


def test_item_count_to_failed():   
    box.clear |should_not| change(box.item_count).to(0)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should not have changed to 0


def test_item_count_to_failed2():    
    box.clear |should| change(box.item_count).to(1)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed to 1, but was changed to 0


def test_item_count_to_failed3():    
    box.clear()
    box.clear |should| change(box.item_count).to(0)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have been changed to 0, but is now 0


def test_item_count_to_passed():    
    box.clear |should_not| change(box.item_count).to(0)


def test_item_count_char_failed():    
    box.clear()
    box.add_items('a', 'b')
    box.item_count()
    # 2
    box.clear |should| change(box.item_count).from_(1).to(0)
    # Traceback (most recent call last):
    #     ...
    # ShouldNotSatisfied: result should have changed from 1 to 0, but was changed from 2 to 0


# Mutable references are supported as expected:
def test_mutable_references():    
    class ClientRepository(object):
        def __init__(self):
            self._clients = []
        def insert(self, client_name):
            self._clients.append(client_name)
        def clients(self):
            return self._clients

    client_repository = ClientRepository()
    (client_repository.insert, 'Paul') |should| change(client_repository.clients)