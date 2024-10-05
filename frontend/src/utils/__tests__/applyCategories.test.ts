import { applyCategories } from '../applyCategories';
import { Product } from '../../types/Product';
import {useProducts} from '../../hooks/useProducts';
describe('test apply categories function', () => {
    it('should return value with price symbol', () => {
        expect(applyCategories(useProducts(), ['Электроника'])).toStrictEqual(useProducts());
    });
});
