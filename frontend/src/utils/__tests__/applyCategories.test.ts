import { applyCategories } from "../applyCategories";
import { Product } from "../../types";

const fixturesProducts: Product[] = [
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
    it('should return all products', () => {
        const result = applyCategories(fixturesProducts, []);

        expect(result.length).toBe(4);
        expect(result).toStrictEqual(fixturesProducts);
    });

    it('should return products from one category', () => {
        const result = applyCategories(fixturesProducts, ['Одежда']);

        expect(result.length).toBe(1);
        expect(result).toStrictEqual(fixturesProducts.slice(1,2));
    });

    it('should return products from few categories', () => {
        const result = applyCategories(fixturesProducts, ['Одежда', 'Для дома']);

        expect(result.length).toBe(2);
        expect(result).toStrictEqual(fixturesProducts.slice(1,3));
    });
});
