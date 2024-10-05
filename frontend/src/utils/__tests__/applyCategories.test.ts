import { Category, Product } from '../../types';
import { applyCategories } from '../applyCategories';

const testProducts: Product[] = [
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

const testCases = [
    { categories: [], expected: testProducts },
    {
        categories: ['Электроника'] as Category[],
        expected: [
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
        ],
    },
    {
        categories: ['Одежда'] as Category[],
        expected: [
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
        ],
    },
    {
        categories: ['Для дома'] as Category[],
        expected: [
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
        ],
    },
    {
        categories: ['Электроника', 'Одежда'] as Category[],
        expected: [
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
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ],
    },
    {
        categories: ['Электроника', 'Для дома'] as Category[],
        expected: [
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
        ],
    },
    {
        categories: ['Одежда', 'Для дома'] as Category[],
        expected: [
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
        ],
    },
    {
        categories: ['Электроника', 'Одежда', 'Для дома'] as Category[],
        expected: testProducts,
    },
];

describe('test applyCategories function', () => {
    test.each(testCases)(
        'applying $categories categories',
        ({ categories, expected }) => {
            expect(applyCategories(testProducts, categories)).toEqual(expected);
        }
    );
});
