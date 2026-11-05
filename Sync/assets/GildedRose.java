package com.gildedrose;

class GildedRose {
    
    private static final String AGED_BRIE = "Aged Brie";
    private static final String BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert";
    private static final String SULFURAS = "Sulfuras, Hand of Ragnaros";
    private static final int MIN_QUALITY = 0;
    private static final int MAX_QUALITY = 50;

    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item : items) {
            switch (item.name) {
                case AGED_BRIE -> updateAgedBrie(item);
                case BACKSTAGE -> updateBackstage(item);
                case SULFURAS -> {}
                default -> updateNormalItem(item);
            }
        }
    }

    private void updateNormalItem(Item item) {
        decreaseQuality(item);
        if (decreaseSellInAndCheck(item)) { decreaseQuality(item);}
    }

    private void updateAgedBrie(Item item) {
        increaseQuality(item);
        if (decreaseSellInAndCheck(item)) { increaseQuality(item);}
    }

    private void updateBackstage(Item item) {
        increaseQuality(item);
        if (item.sellIn < 11) { increaseQuality(item);}
        if (item.sellIn < 6) { increaseQuality(item);}
        if (decreaseSellInAndCheck(item)) {item.quality = MIN_QUALITY;}
    }

    private void increaseQuality(Item item) {
        if (item.quality < MAX_QUALITY) {item.quality++;}
    }

    private void decreaseQuality(Item item) {
        if (item.quality > MIN_QUALITY) {item.quality--;}
    }

    private boolean decreaseSellInAndCheck(Item item) {return (--item.sellIn < 0);}
}
