import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return added categories', () => {
        expect(updateCategories([], 'Для дома')).toEqual(['Для дома']);
        expect(updateCategories(['Для дома', 'Электроника'], 'Одежда')).toEqual(
            ['Для дома', 'Электроника', 'Одежда']
        );
    });
    it('should return cutted categories', () => {
        expect(updateCategories(['Для дома'], 'Для дома')).toEqual([]);
        expect(
            updateCategories(['Для дома', 'Электроника', 'Одежда'], 'Одежда')
        ).toEqual(['Для дома', 'Электроника']);
    });
});
