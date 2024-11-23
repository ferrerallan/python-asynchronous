class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)
        print(f"Observer attached. Total observers: {len(self._observers)}")  # New print statement

    def detach(self, observer):
        self._observers.remove(observer)
        print(f"Observer detached. Total observers: {len(self._observers)}")  # New print statement

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Observer:
    def update(self, subject):
        raise NotImplementedError


class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        print(f"Subject state changing from '{self._state}' to '{state}'")  # New print statement
        self._state = state
        self.notify()


class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer notified: Subject state changed to {subject.state}")



subject = ConcreteSubject("Initial State")
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.state = "New State"