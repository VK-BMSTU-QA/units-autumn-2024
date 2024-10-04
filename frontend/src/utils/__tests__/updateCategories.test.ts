import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

interface UpdateCategoriesTestCase {
    currentCategories: Category[];
    changedCategory: Category;
    expected: Category[];
}

const testCases: UpdateCategoriesTestCase[] = [
    {
        currentCategories: ['Одежда', 'Для дома'],
        changedCategory: 'Электроника',
        expected: ['Одежда', 'Для дома', 'Электроника'],
    },
    {
        currentCategories: ['Одежда', 'Для дома'],
        changedCategory: 'Для дома',
        expected: ['Одежда'],
    },
];

const testFn = ({
    currentCategories,
    changedCategory,
    expected,
}: UpdateCategoriesTestCase) => {
    const result = updateCategories(currentCategories, changedCategory);
    expect(result).toStrictEqual(expected);
};

test.each(testCases)('currentCategories: %o; changedCategory: %s', testFn);
