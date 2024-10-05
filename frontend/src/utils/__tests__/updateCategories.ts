import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('updateCategories function', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома'];

    it('should add a new category if not already in the list', () => {
        const result = updateCategories(currentCategories, 'Одежда');
        expect(result).toEqual(['Электроника', 'Для дома', 'Одежда']); 
    });

    it('should remove a category if it exists in the list', () => {
        const result = updateCategories(currentCategories, 'Электроника');
        expect(result).toEqual(['Для дома']);
    });

    it('should return the same list if category does not exist', () => {
        const result = updateCategories(currentCategories, 'Одежда');
        expect(result).toEqual([...currentCategories, 'Одежда']);
    });

    it('should return the same list if category is removed and then added back', () => {
        let result = updateCategories(currentCategories, 'Электроника');
        result = updateCategories(result, 'Электроника');
        expect(result).toEqual(expect.arrayContaining(currentCategories));
    });
    
});
