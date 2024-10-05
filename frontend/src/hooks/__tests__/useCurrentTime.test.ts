import { act, renderHook } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from '../useCurrentTime';

describe('test useCurrentTime', () => {
    let originalDate: DateConstructor;

    beforeAll(() => {
        jest.useFakeTimers();
        originalDate = global.Date;
        const mockDate = new originalDate('2024-01-01T12:42:21Z');
        global.Date = jest.fn(() => mockDate) as unknown as DateConstructor;
        global.Date.prototype.toLocaleTimeString = jest.fn(() => '12:42:21');
    });

    afterEach(() => {
        global.Date = originalDate;
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should render correctly', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('12:42:21');
    });

    it('should update time every second', () => {
        const { result } = renderHook(() => useCurrentTime());
        const initialTime = result.current;

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const currentTime = result.current;

        expect(initialTime).not.toBe(currentTime);
    });

    it('should use Date function', () => {
        const { result } = renderHook(() => useCurrentTime());
        const data = result.current;

        expect(data).toBe(new Date().toLocaleTimeString('ru-RU'));
    });
});
