import { applyCategories } from '../applyCategories';
import { Product } from '../../types';
import { Category } from '../../types';

const Products: Product[] = [
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

describe('test applyСategories', () => {
    it('should return all products', () => {
        const expected_Products: Product[] = [
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

        const category: Category[] = [];

        expect(applyCategories(Products, category)).toStrictEqual(
            expected_Products
        );
    });



    it('should return lamp', () => {
        const expected_Products: Product[] = [
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
        ];

        const category: Category[] = ['Для дома'];

        expect(applyCategories(Products, category)).toStrictEqual(
            expected_Products
        );
    });



    it('should return nothing 1', () => {
        const expected_Products: Product[] = [
        ];

        const category: Category[] = ['Электроника', 'Для дома', 'Одежда'];

        expect(applyCategories([], category)).toStrictEqual(
            expected_Products
        );
    });

    it('should return nothing double Электроника', () => {
        const expected_Products: Product[] = [
        ];

        const category: Category[] = ['Электроника', 'Электроника'];

        expect(applyCategories([], category)).toStrictEqual(
            expected_Products
        );
    });

});