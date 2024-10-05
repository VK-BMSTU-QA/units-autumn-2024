import { applyCategories } from '../applyCategories';
import { Product } from '../../types';

describe('applyCategories function', () => {
    const products: Product[] = [
        { id: 1, name: 'Product 1', description: 'Description 1', price: 1000, category: 'Электроника' },
        { id: 2, name: 'Product 2', description: 'Description 2', price: 500, category: 'Одежда' },
        { id: 3, name: 'Product 3', description: 'Description 3', price: 1500, category: 'Для дома' },
    ];

    it('should return all products if categories array is empty', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products); 
    });

    it('should return products that match categories', () => {
        const result = applyCategories(products, ['Электроника']);
        expect(result).toEqual([
            { id: 1, name: 'Product 1', description: 'Description 1', price: 1000, category: 'Электроника' },
        ]); 
    });

    it('should return products from multiple categories', () => {
        const result = applyCategories(products, ['Электроника', 'Одежда']);
        expect(result).toEqual([
            { id: 1, name: 'Product 1', description: 'Description 1', price: 1000, category: 'Электроника' },
            { id: 2, name: 'Product 2', description: 'Description 2', price: 500, category: 'Одежда' },
        ]); 
    });

    it('should return products with all available categories', () => {
        const result = applyCategories(products, ['Электроника', 'Одежда', 'Для дома']);
        expect(result).toEqual(products); 
    });
});
