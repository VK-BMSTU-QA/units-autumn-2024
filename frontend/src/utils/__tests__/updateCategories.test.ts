import {Category} from '../../types';
import { updateCategories } from '../updateCategories';


describe('test updateСategory', () => {
    it('should add Электроника', () => {
        const categories: Category[] = [];
        const changedCategory: Category = 'Электроника';
        const expectedCategories: Category[] = ['Электроника'];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });
    it('should remove Электроника', () => {
        const categories: Category[] = ['Электроника'];
        const changedCategory: Category = 'Электроника';
        const expectedCategories: Category[] = [];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });

    it('should remove Для дома', () => {
        const categories: Category[] = ['Для дома','Электроника'];
        const changedCategory: Category = 'Для дома';
        const expectedCategories: Category[] = ['Электроника'];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });

    it('should add Для дома', () => {
        const categories: Category[] = ['Электроника'];
        const changedCategory: Category = 'Для дома';
        const expectedCategories: Category[] = ['Электроника', 'Для дома'];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });

    it('should add Одежда', () => {
        const categories: Category[] = [];
        const changedCategory: Category = 'Одежда';
        const expectedCategories: Category[] = ['Одежда'];

        expect(updateCategories(categories, changedCategory)).toStrictEqual(
            expectedCategories
        );
    });
});