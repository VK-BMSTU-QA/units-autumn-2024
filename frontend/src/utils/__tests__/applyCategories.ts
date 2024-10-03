import {applyCategories} from '../applyCategories';
import type {Product, Category} from '../../types';

// Пример данных для тестирования
const mockProducts: Product[] = [
    {id: 1, name: "name", description: "name", price: 123, priceSymbol: '$', imgUrl: "name", category: 'Электроника'},
    {id: 2, name: "name", description: "name", price: 123, priceSymbol: '$', imgUrl: "name", category: 'Для дома'},
    {id: 3, name: "name", description: "name", price: 123, priceSymbol: '$', imgUrl: "name", category: 'Одежда'},
];

describe('applyCategories', () => {
    test('returns all products if no categories are provided', () => {
        const result = applyCategories(mockProducts, []);
        expect(result).toEqual(mockProducts);  // Ожидаем, что все продукты будут возвращены
    });

    test('filters products by provided categories', () => {
        const result = applyCategories(mockProducts, ['Одежда']);
        expect(result).toEqual([
            {
                id: 3,
                name: "name",
                description: "name",
                price: 123,
                priceSymbol: '$',
                imgUrl: "name",
                category: 'Одежда'
            },
        ]);
    });

    test('filters products by provided categories', () => {
        const result = applyCategories(mockProducts, ['Одежда', 'Для дома']);
        expect(result).toEqual([
            {
                id: 2,
                name: "name",
                description: "name",
                price: 123,
                priceSymbol: '$',
                imgUrl: "name",
                category: 'Для дома'
            },
            {
                id: 3,
                name: "name",
                description: "name",
                price: 123,
                priceSymbol: '$',
                imgUrl: "name",
                category: 'Одежда'
            },
        ]);
    });

    test('filters products by provided categories', () => {
        const result = applyCategories(mockProducts, ['Одежда', 'Для дома', "Электроника"]);
        expect(result).toEqual([
            {
                id: 1,
                name: "name",
                description: "name",
                price: 123,
                priceSymbol: '$',
                imgUrl: "name",
                category: 'Электроника'
            },
            {
                id: 2,
                name: "name",
                description: "name",
                price: 123,
                priceSymbol: '$',
                imgUrl: "name",
                category: 'Для дома'
            },
            {
                id: 3,
                name: "name",
                description: "name",
                price: 123,
                priceSymbol: '$',
                imgUrl: "name",
                category: 'Одежда'
            },
        ]);
    });

});
