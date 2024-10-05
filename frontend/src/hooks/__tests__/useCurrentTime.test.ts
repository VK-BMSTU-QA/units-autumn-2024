import { act, renderHook } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from '../useCurrentTime';

describe('test useCurrentTime', () => {
    let originalDate: DateConstructor;

    beforeAll(() => {
        jest.useFakeTimers(); // time stop
        originalDate = global.Date;
        const mockDate = new originalDate('2020-02-02T12:42:21Z');
        global.Date = jest.fn(() => mockDate) as unknown as DateConstructor;
        global.Date.prototype.toLocaleTimeString = jest.fn(() => '12:42:21');
    });

    afterEach(() => {
        global.Date = originalDate;
    });

    afterAll(() => {
        jest.useRealTimers();
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

    it('should update time correctly after multiple seconds', () => {
        const { result } = renderHook(() => useCurrentTime());
        const initialTime = result.current;

        act(() => {
            jest.advanceTimersByTime(5000); // Move time forward by 5 seconds
        });

        const currentTime = result.current;

        expect(initialTime).not.toBe(currentTime);
        expect(currentTime).toBe(new Date('2020-02-02T12:42:26Z').toLocaleString());
    });

    it('should render correctly', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('12:42:21');
    });
    it('should use Date function', () => {
        const { result } = renderHook(() => useCurrentTime());
        const data = result.current;

        expect(data).toBe(new Date().toLocaleTimeString('ru-RU'));
    });


});