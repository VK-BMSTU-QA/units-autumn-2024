import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

export const testProducts = (): Product[] => [
    {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    },
    {
        id: 2,
        name: 'Костюм гуся',
        description: 'Запускаем гуся, работяги',
        price: 1000,
        priceSymbol: '₽',
        category: 'Одежда',
    },
    {
        id: 3,
        name: 'Настольная лампа',
        description: 'Говорят, что ее использовали в pixar',
        price: 699,
        category: 'Для дома',
        imgUrl: '/lamp.png',
    },
    {
        id: 4,
        name: 'Принтер',
        description: 'Незаменимая вещь для студента',
        price: 7000,
        category: 'Электроника',
    },
];

describe('test apply categories function', () => {
    const testCases = [
        {
            categories: ["Для дома"],
            expected: testProducts().slice(2, 3),
        },
        {
            categories: ["Для дома", "Одежда"],
            expected: testProducts().slice(1, 3),
        },
        {
            categories: ["Для дома", "Одежда", "Электроника"],
            expected: testProducts(),
        },
        {
            categories: [],
            expected: testProducts(),
        },
    ];

    testCases.forEach(({ categories, expected }) => {
        it(`should return products for categories: ${JSON.stringify(categories)}`, () => {
            expect(applyCategories(testProducts(), categories as Category[])).toStrictEqual(expected);
        });
    });
});
