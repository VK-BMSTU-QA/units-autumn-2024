import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

describe('applyCategories', () => {
    const product1: Product = {
        name: 'name',
        description: 'description',
        id: 1,
        category: 'Одежда',
        price: 100,
    };
    const product2: Product = {
        name: 'name2',
        description: 'description2',
        id: 2,
        category: 'Для дома',
        price: 200,
    };
    const product3: Product = {
        name: 'name3',
        description: 'description3',
        id: 3,
        category: 'Электроника',
        price: 300,
    };
    test.each([
        [
            'should return all products when no categories provided',
            [product1, product2],
            [],
            [product1, product2],
        ],
        [
            'should filter products by categories',
            [product1, product2, product3],
            ['Электроника' as Category, 'Одежда' as Category],
            [product1, product3],
        ],
        [
            'should return empty array if no products match categories',
            [product1, product2],
            ['Электроника' as Category],
            [],
        ],
    ])('%s', (_, products, categories, expected) => {
        const result = applyCategories(products, categories);
        expect(result).toEqual(expected);
    });
});
