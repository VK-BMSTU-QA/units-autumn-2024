import { applyCategories } from '../applyCategories';
import { expectedProducts as products }  from '../../mocks/mocks';

describe('applyCategories', () => {

    it('должен вернуть все продукты, если категории не указаны', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    it('должен вернуть продукты только из категории Электроника', () => {
        const result = applyCategories(products, ['Электроника']);
        expect(result).toEqual([
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
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
    });

    it('должен вернуть продукты из категорий Электроника и Для дома', () => {
        const result = applyCategories(products, ['Электроника', 'Для дома']);
        expect(result).toEqual([
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
        ]);
    });

    it('должен вернуть продукты только из категории Одежда', () => {
        const result = applyCategories(products, ['Одежда']);
        expect(result).toEqual([
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
        ]);
    });
});
