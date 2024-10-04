import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categor function', () => {
    it('should include category', () => {
        const categories: Category[] = [];
        const changedCategory: Category = 'Для дома';
        const expectedCategories: Category[] = ['Для дома'];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });
    it('should include category', () => {
        const categories: Category[] = ['Для дома'];
        const changedCategory: Category = 'Для дома';
        const expectedCategories: Category[] = [];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });
});
