import { useCurrentTime } from './useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('Current time test', () => {
    it('should render current time', () => {
        // позволяет управлять временем
        jest.useFakeTimers();
        // устанавливаем время
        jest.setSystemTime(new Date('2021-12-12T12:00:00').getTime());
        const { result } = renderHook(() => useCurrentTime());
        const time = new Date('2021-12-12T12:00:00').toLocaleTimeString(
            'ru-RU'
        );
        expect(result.current).toBe(time);
    });
});
