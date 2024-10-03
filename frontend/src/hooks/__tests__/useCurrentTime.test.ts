import { renderHook, act } from "@testing-library/react";
import { useCurrentTime } from "../useCurrentTime";

jest.useFakeTimers();

describe('test use current time hook', () => {
    it('should set current time', () => {
        jest.setSystemTime(new Date('2020-01-01 11:00:00'));

        const { result } = renderHook(useCurrentTime);

        expect(result.current).toBe('11:00:00');
    });

    it('should update current time', () => {
        jest.setSystemTime(new Date('2020-01-01 11:00:00'));

        const { result } = renderHook(useCurrentTime);

        act(() => jest.advanceTimersByTime(1000));
        expect(result.current).toBe('11:00:01');
    });
});
