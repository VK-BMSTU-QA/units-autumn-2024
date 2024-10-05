import { useProducts } from '../useProducts';

describe('useProducts hook', () => {
    it('should return an array of products', () => {
        const products = useProducts();

        expect(products).toBeInstanceOf(Array);
        expect(products).toHaveLength(4);

        products.forEach(product => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('category');

            if (product.imgUrl) {
                expect(product).toHaveProperty('imgUrl');
            }
        });
    });
});