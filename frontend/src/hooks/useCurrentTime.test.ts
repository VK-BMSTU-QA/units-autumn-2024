import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

describe('useCurrentTime Hook', () => {
    beforeAll(() => {
        jest.useFakeTimers();
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should display time coorectly', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toMatch(/^\d{2}:\d{2}:\d{2}$/);
    });

    it('should return current time', () => {
        const settedTime = new Date('2024-01-01 21:00:00');
        jest.setSystemTime(settedTime);

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe('21:00:00');
    });

    it('should update time every second', () => {
        const settedTime = new Date('2024-01-01 21:00:00');
        jest.setSystemTime(settedTime);

        const { result } = renderHook(() => useCurrentTime());

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).not.toBe('21:00:00');
    });
});
