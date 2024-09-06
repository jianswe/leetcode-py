from heap.MedianFinder import MedianFinder

def test_MedianFinder():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5 
    mf.addNum(3)
    assert mf.findMedian() == 2.0 
