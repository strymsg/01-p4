import uuid


if __name__ == '__main__':
    print('Testing module')
    print('generation')
    for i in range(30):
        print(uuid.uuid4().hex)

    generated = {}
    print('Testing 10000000 generation')
    for i in range(10000000):
        identifier = uuid.uuid4().hex
        if generated.get(identifier, None) is None:
            generated[identifier] = True
        else:
            print(f'Error duplicated identifier {identifier}')
        if i%100000 == 0:
            print(f'{i} tests passed...')
    print('Done.')

