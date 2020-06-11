<template>
    <div class="container">
        <div>
            <h1>Nhóm 5 - Tìm Kiếm Điện Thoại</h1>
            <br />
            <input v-model="query" class="search_input" type="text" placeholder="Type anything ..." />
            <button @click="submit(0)">Search</button>
            <button @click="hideFilter = !hideFilter ">Filter</button>
        </div>
        <div class="container-filter">
            <ul class="filter filter-price" v-if="hideFilter">
                <li
                    v-for="(price,index) in listPrices"
                    :key="index"
                    @click="filterPrice=index;submit(pageCurrent)"
                >
                    <a>{{price.name}}</a>
                </li>
            </ul>
            <ul class="filter filter-location" v-if="hideFilter">
                <li
                    v-for="(loc,index) in listLocations"
                    :key="index"
                    @click="filterLocation=index;submit(pageCurrent)"
                >
                    <a>{{loc.name}}</a>
                </li>
            </ul>
        </div>
        <div class="container-result" v-if="data != null">
            <p class="result">Kết quả Tìm kiếm Với {{query}} - Giá:{{listPrices[filterPrice].name}} - Địa chỉ: {{listLocations[filterLocation].name}}</p>
            <div class="container-items">
                <div class="items" v-for="item in data" :key="item.id">
                    <a
                        :href="'https://shopee.vn/'+getLink(item.name[0])+'.'+item.shopid[0]+'.'+item.id"
                        target="_blank"
                    >
                        <img width="100%" :src="'https://cf.shopee.vn/file/'+item.image[0]" />
                        <div class="name-item">{{item.name[0]}}</div>
                        <div class="address-item">Địa chỉ: {{item.location[0]}}</div>
                        <div
                            class="price-item"
                        >Giá: {{item.price[0].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1.")}}</div>
                        <div class="rate-item">Đánh giá: {{item.rating_star[0]}}</div>
                    </a>
                </div>
            </div>
        </div>
        <div class="pagination">
            <span>
                <span :class="{hidden : (pageCurrent==0)}" @click="submit(pageCurrent-1)">&laquo;</span>
            </span>
            <span v-for="page in pages" :key="page">
                <span
                    v-if="page >= pageCurrent-3 && page < pageCurrent+4"
                    @click="submit(page)"
                    :class="{active : (pageCurrent==page)}"
                >{{page+1}}</span>
            </span>
            <span>
                <span
                    :class="{hidden : (pageCurrent >= numPage-1)}"
                    @click="submit(pageCurrent+1)"
                >&raquo;</span>
            </span>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "SearchHome",
    data() {
        return {
            data: null,
            query: "",
            numFound: 0,
            numPage: 0,
            pageCurrent: 0,
            pages: [],
            hideFilter: false,
            filterPrice: 0,
            filterLocation: 0,

            listPrices: [
                {
                    name: "Tất cả mức giá",
                    query: ""
                },
                {
                    name: "< 2.000.000",
                    query: "price:[*%20TO%202000000]"
                },
                {
                    name: "2.000.000 - 5.000.000",
                    query: "price:[2000000%20TO%205000000]"
                },
                {
                    name: "5.000.000 - 10.000.000",
                    query: "price:[5000000%20TO%2010000000]"
                },
                {
                    name: "> 10.000.000",
                    query: "price:[10000000%20TO%20*]"
                }
            ],
            listLocations: [
                {
                    name: "Tất cả các vùng",
                    query: ""
                },
                {
                    name: "Hà Nội",
                    query: "hà%20nội+"
                },
                {
                    name: "Hồ Chí Minh",
                    query: "ho%20chi%20minh+"
                },
                {
                    name: "Đà nẵng",
                    query: "đà%20nẵng+"
                },
                {
                    name: "Cần Thơ",
                    query: "cần%20thơ+"
                }
            ]
        };
    },
    methods: {
        async submit(page) {
            let headers = {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            };
            let res = await axios.get(
                "http://localhost:8983/solr/phone-data/select?indent=on&" +
                    "q=" +
                    this.query + " " + this.listLocations[this.filterLocation].query +
                    "&wt=json" +
                    "&start=" +
                    page * 10 +
                    "&fq=" +
                    this.listPrices[this.filterPrice].query,                    
                headers
            );
            if (res.status !== 200) {
                alert("Đã xảy ra lỗi !!!");
            }

            this.data = res.data.response.docs;
            console.log(this.data);
            this.numFound = res.data.response.numFound;
            this.numPage = this.numFound / 10;
            this.pageCurrent = page;
            this.pages = [];
            for (let i = 0; i < this.numPage; i++) this.pages.push(i);
            console.log(res);
        },
        getLink(name) {
            let regex = "+-/%@";
            let link = name.split(" ");
            for (let s in link) {
                if (regex.includes(link[s])) link[s] = "-";
            }
            link = link.join(" ");
            link = link.replace(/ /g, "-");
            return link + "-i";
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
    font-weight: normal;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
    text-decoration: none;
    cursor: pointer;
}
button {
    border: solid 2px #ee4d2d;
    border-radius: 10px;
    padding: 20px;
    background-color: #ee4d2d;
    color: #ffffff;
}
button:hover {
    background-color: #4caf50;
    border: solid 2px #4caf50;
}
.search_input {
    width: 50%;
    border: solid 2px #ee4d2d;
    border-radius: 10px;
    padding: 20px;
}
input:focus {
    outline: none;
    border: solid 2px #ee4d2d;
}
.container-result {
    justify-content: center;
}
.result {
    height: 28px;
    font-family: SFD-Medium;
    font-size: 20px;
    line-height: 28px;
    color: #f77638;
}
.container-items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.items {
    border: 1px solid transparent;
    border-radius: 10px;
    padding-right: 0.3125rem;
    padding-left: 0.3125rem;
    max-width: 200px;
    margin: 10px;
    background: #fff;
}
.items:hover {
    border: 1px solid #ee4d2d;
    border-radius: 10px;
}
.name-item {
    padding: 10px 0px;
    font-weight: bold;
}
.address-item {
    padding: 10px 0px;
}
.pagination {
    margin-top: 50px;
    display: inline-block;
}

.pagination span span {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
    transition: background-color 0.3s;
    border: 1px solid #ddd;
    margin: 0 4px;
    cursor: pointer;
}

.pagination span span.active {
    background-color: #4caf50;
    color: white;
    border: 1px solid #4caf50;
}
.hidden {
    visibility: hidden;
}
.container-filter {
    margin: 50px;
    /* text-align: left; */
    display: flex;
    flex-wrap: wrap;
}
.filter {
    display: flex;
    flex-direction: column;
    width: 50%;
}
.filter li {
    margin: 10px;    
}
.filter li:hover {
    border: 1px solid #ee4d2d;
    padding: 5px;
}
</style>
