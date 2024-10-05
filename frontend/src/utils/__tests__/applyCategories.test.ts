import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

let product_electronics : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Электроника',
}

let product_clothes : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
}

let product_home : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Для дома'
}

let product_home_2 : Product = {
    name: 'product2',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Для дома'
}

describe('test apply categories function', () => {
    it('should return products with chosen categories', () => {
        expect(applyCategories([product_clothes, product_electronics, product_home], ['Электроника'])).toStrictEqual([product_electronics]);
        expect(applyCategories([product_clothes, product_electronics, product_home], ['Электроника', 'Для дома'])).toStrictEqual([product_electronics, product_home]);
        expect(applyCategories([product_home_2, product_electronics, product_home], ['Для дома'])).toStrictEqual([product_home_2, product_home]);
    });
    
    it('should return all products when no categories are chosen', () => {
        expect(applyCategories([product_clothes, product_electronics, product_home], [])).toStrictEqual([product_clothes, product_electronics, product_home]);
    })
    
    it('should return nothing if no products with such category', () => {
        expect(applyCategories([product_clothes, product_home], ['Электроника'])).toStrictEqual([]);
    })
});
