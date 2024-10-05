import { useProducts } from '../useProducts';

describe('test use products hook', () => {
    test('should return an array of products with correct structure', () => {
        const products = useProducts();

        expect(products).toBeInstanceOf(Array);
        expect(products.length).toEqual(4);

        products.forEach((product) => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('category');
        });
    });

    test('should return an array with correct length', () => {
        const products = useProducts();

        expect(products).toBeInstanceOf(Array);
        expect(products.length).toEqual(4);
    });
});