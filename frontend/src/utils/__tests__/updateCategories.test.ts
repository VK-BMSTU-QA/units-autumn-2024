import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('test updateCategories function', () => {
    const initialCategories: Category[] = ['Электроника', 'Для дома'];

    it('should add new category when it does not exist in current categories', () => {
        const newCategory: Category = 'Одежда';
        const expectedCategories = [...initialCategories, newCategory];
        const result = updateCategories(initialCategories, newCategory);
        expect(result).toEqual(expectedCategories);
    });

    it('should remove existing category from current categories', () => {
        const categoryToRemove: Category = 'Для дома';
        const expectedCategories = initialCategories.filter(
            (category) => category !== categoryToRemove
        );
        const result = updateCategories(initialCategories, categoryToRemove);
        expect(result).toEqual(expectedCategories);
    });

    it('should remove existing category when adding it again', () => {
        const existingCategory: Category = 'Электроника';
        const expectedCategories = initialCategories.filter(
            (category) => category !== existingCategory
        );
        const result = updateCategories(initialCategories, existingCategory);
        expect(result).toEqual(expectedCategories);
    });

    it('should handle empty initial categories correctly', () => {
        const newCategory: Category = 'Одежда';
        const result = updateCategories([], newCategory);
        expect(result).toEqual([newCategory]);
    });
});
