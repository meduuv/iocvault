from iocvault import classify, normalize

def test_classify():
    assert classify("8.8.8.8") == "ip"
    assert classify("A" * 64) == "sha256"

def test_normalize_deduplicates():
    assert [x["value"] for x in normalize([" EXAMPLE.COM", "example.com", "x.test"])] == ["example.com", "x.test"]
