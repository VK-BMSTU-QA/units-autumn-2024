import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

const emptyCategories: Category[] = [];
const clothesCategory: Category = 'Одежда';
const clothes: Category[] = ['Одежда'];

describe('test update categories function', () => {
    it.each([
        [emptyCategories, clothesCategory, clothes],
        [clothes, clothesCategory, emptyCategories],
    ])(
        'should return updated categories',
        (categories, category, updatedCategories) => {
            expect(updateCategories(categories, category)).toStrictEqual(
                updatedCategories
            );
        }
    );
});