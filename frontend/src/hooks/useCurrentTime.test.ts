import { act, renderHook } from "@testing-library/react";
import { useCurrentTime } from "./useCurrentTime";

describe('test use current time function', () => {
    beforeAll(()=>{
        jest.useFakeTimers();
    });
    afterAll(()=>{
        jest.useRealTimers();
    })
    it('should return current time', () => {
        const testingTime = renderHook(() => useCurrentTime());
        const expectedTime = new Date().toLocaleTimeString('ru-RU');
        expect(testingTime.result.current).toBe(expectedTime);
    });

    it('should update every second', () => {
        const testingTime = renderHook(() => useCurrentTime());
        const resultFirst = testingTime.result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        const resultSecond = testingTime.result.current;
        expect(resultFirst).not.toBe(resultSecond);
    });
});