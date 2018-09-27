import inspect
import time


class Promise:
    # todo raise if no catch

    def __init__(self):
        self.exception = False
        self.args = None
        self.func = None

    def _exec(self):
        if inspect.signature(self.func).parameters:
            self.args = self.func(self.args)
        else:
            self.args = self.func()

    def then(self, func):
        self.func = func
        if self.exception is False:
            try:
                self._exec()
            except Exception as e:
                self.exception = e
        else:
            exception = self.exception
            self.exception = None
            raise exception
        return self

    def catch(self, func):
        self.func = func
        if self.exception:
            self._exec()
            self.exception = False
        return self

    def __repr__(self):
        return 'Promise <pending>'


if __name__ == '__main__':
    def run(param) -> Promise:
        print('run', param)
        return Promise()

    p = run('lol')\
        .then(lambda: 44)\
        .then(lambda x: 55)\
        .then(lambda x: print(1 / 0, x)) \
        .catch(lambda x: print("caught", x)) \
        .then(lambda: 'marche')
    p.then(lambda x: print(x))

    # time.sleep(3)
    print(p)

