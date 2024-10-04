import React from 'react';
import { act, render, renderHook } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime test', () => {
    let originalDate: DateConstructor;

    beforeAll(() => {
        jest.useFakeTimers();

        originalDate = global.Date;

        const mockDate = new originalDate('2024-01-01T12:00:00Z');

        global.Date = jest.fn(() => mockDate) as unknown as DateConstructor;

        global.Date.prototype.toLocaleTimeString = jest.fn(() => '12:00:00');
    });

    afterEach(() => {
        global.Date = originalDate;
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should render correctly', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('15:00:00');
    });
    it('should use Date function', () => {
        const { result } = renderHook(() => useCurrentTime());
        const data = result.current;

        expect(data).toBe(new Date().toLocaleTimeString('ru-RU'));
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
});
