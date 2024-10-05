import { useCurrentTime } from './useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('Current time test', () => {
    it('should render current time', () => {
        // позволяет управлять временем
        jest.useFakeTimers();
        const { result } = renderHook(() => useCurrentTime());
        const time = new Date().toLocaleTimeString('ru-RU');
        expect(result.current).toBe(time);
    });
});
