import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

let home : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Для дома'
}

let home_2 : Product = {
    name: 'product2',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Для дома'
}

let clothes : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
}

let electronics : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Электроника',
}

describe('test for the category application function', () => {
    it('returns products from the selected category', () => {
        expect(applyCategories([clothes, home], ['Электроника'])).toStrictEqual([]);
        expect(applyCategories([clothes, electronics, home], ['Одежда', 'Для дома'])).toStrictEqual([clothes, home]);
        expect(applyCategories([clothes, electronics, home], ['Электроника', 'Для дома'])).toStrictEqual([electronics, home]);
        expect(applyCategories([clothes, electronics, home], ['Электроника'])).toStrictEqual([electronics]);
        expect(applyCategories([clothes, electronics, home], [])).toStrictEqual([clothes, electronics, home]);
        expect(applyCategories([home_2, electronics, home], ['Для дома'])).toStrictEqual([home_2, home]);
    });
});