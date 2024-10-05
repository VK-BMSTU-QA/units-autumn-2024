import { useCurrentTime } from '../useCurrentTime';
import { cleanup, renderHook, act } from '@testing-library/react';

jest.useFakeTimers();

describe('useCurrentTime hook', () => {
    afterEach(() => {
        cleanup();
        jest.clearAllMocks();
        jest.clearAllTimers();
    });

    it('should return the initial mocked time', () => {
        const mockToLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue('2000-01-01T01:00:00');

        const { result } = renderHook(() => useCurrentTime());

        expect(mockToLocale).toHaveBeenCalledTimes(1);
        expect(result.current).toBe('2000-01-01T01:00:00');
    });

    it('should update the time after the interval', () => {
        let mockToLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue('2000-01-01T01:00:00');

        const { result } = renderHook(() => useCurrentTime());

        expect(mockToLocale).toHaveBeenCalledTimes(1);
        expect(result.current).toBe('2000-01-01T01:00:00');

        mockToLocale = mockToLocale.mockReturnValue('new mock locale');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(mockToLocale).toHaveBeenCalledTimes(3);
        expect(result.current).toBe('new mock locale');
    });
});
