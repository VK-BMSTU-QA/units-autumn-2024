import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

const testDate = new Date('2024-03-09T00:00:00.000Z');

describe('test useCurrentTime hook', () => {
    it('should return current time', () => {
        jest.spyOn(global, 'Date').mockImplementationOnce(() => testDate);
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toStrictEqual(
            testDate.toLocaleTimeString('ru-RU')
        );
    });
});