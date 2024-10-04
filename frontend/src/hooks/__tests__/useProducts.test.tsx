import { useCurrentTime } from '../useCurrentTime';
import { cleanup, renderHook, act } from '@testing-library/react';

jest.mock('..');

describe('test use current time function', () => {
    afterEach(() => {
        cleanup;
    });
    it('should return fake previously setted time', () => {
        jest.useFakeTimers().setSystemTime(new Date('2020-01-01T01:00:00'));

        const { result } = renderHook(() => useCurrentTime());
        const currentTime = result.current;

        expect(currentTime).toEqual('01:00:00');
    });
    it('should update fake previously setted time', () => {
        jest.useFakeTimers().setSystemTime(new Date('2020-01-01T01:00:00'));

        const { result } = renderHook(() => useCurrentTime());

        act(() => {
            jest.advanceTimersByTime(3000);
        });

        expect(result.current).toEqual('01:00:03');
    });
});
