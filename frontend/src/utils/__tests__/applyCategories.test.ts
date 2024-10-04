import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    it('should return initial empty products by given empty array', () => {
        expect(applyCategories([], [])).toEqual([]);
    });
    it('should return initial empty products by given empty array', () => {
        expect(
            applyCategories(
                [
                    {
                        id: 2,
                        name: 'Aleshka',
                        description: 'BMSTU Student',
                        price: 0,
                        category: 'Для дома',
                    },
                ],
                []
            )
        ).toEqual([
            {
                id: 2,
                name: 'Aleshka',
                description: 'BMSTU Student',
                price: 0,
                category: 'Для дома',
            },
        ]);
    });
    it('should return an empty array by given not empty array', () => {
        expect(
            applyCategories(
                [
                    {
                        id: 2,
                        name: 'Aleshka',
                        description: 'BMSTU Student',
                        price: 0,
                        category: 'Для дома',
                    },
                ],
                ['Электроника', 'Одежда']
            )
        ).toEqual([]);
    });
    it('should return not an empty array', () => {
        expect(
            applyCategories(
                [
                    {
                        id: 2,
                        name: 'Aleshka',
                        description: 'BMSTU Student',
                        price: 0,
                        category: 'Для дома',
                    },
                ],
                ['Для дома', 'Электроника', 'Одежда']
            )
        ).toEqual([
            {
                id: 2,
                name: 'Aleshka',
                description: 'BMSTU Student',
                price: 0,
                category: 'Для дома',
            },
        ]);
    });
});
