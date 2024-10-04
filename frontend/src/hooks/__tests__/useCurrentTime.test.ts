import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test useCurrentTime hook', () => {
    beforeAll(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('17 Jan 2004 12:34:56').getTime());
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    test('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toEqual('12:34:56');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(result.current).toEqual('12:34:57');
    });
});