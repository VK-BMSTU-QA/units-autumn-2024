import { applyCategories } from '../applyCategories';
import {Product, Category} from "../../types";

describe('applyCategories function test', () => {
    const products: Product[] = [
        { id: 1, name: 'Product 1', category: 'Электроника', description: 'Лучший товар 1',price: 100},
        { id: 2, name: 'Product 2', category: 'Для дома', description: 'Лучший товар 2',price: 200},
        { id: 3, name: 'Product 3', category: 'Одежда' , description: 'Лучший товар 3',price: 300},
        { id: 4, name: 'Product 4', category: 'Одежда' , description: 'Лучший товар 4',price: 400},
    ];

    const categories: Category[] = ['Электроника', 'Одежда'];

    it('should return all products if categories array is empty', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    it('should return empty array if products array is empty', () => {
        const result = applyCategories([], categories);
        expect(result).toEqual([]);
    });

    it('should return empty array if both products and categories arrays are empty', () => {
        const result = applyCategories([], []);
        expect(result).toEqual([]);
    });
});
