<template>
    <div class="container">
        <form>
            <div>
                <h1>Tìm kiếm điện thoại - So sánh giá</h1>
            </div>
            <form @submit="submit">
                <label></label>
                <input class="search_input" type="text" placeholder="Type anything ..." />
            </form>
        </form>
        <div class="container-items" v-if="data != null">
            <div class="items">
                <div class="name-item">{{data.name}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "SearchHome",
    data() {
        return {
            data: null
        };
    },
    methods: {
        async submit() {
            let headers = {
              'Access-Control-Allow-Origin': '*'
            }
            await axios({
                method: "get",
                url: "http://localhost:8983/solr/BTL/select?q=*%3A*&wt=json",
                headers: headers
            })
                .then(function(response) {
                    console.log(response);
                    this.data = response.data;
                })
                .catch(function(response) {
                    console.log(response);
                });            
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
}
.search_input {
    width: 50%;
    border: solid 2px #42b983;
    border-radius: 20px;
    padding: 20px;
}
input:focus {
    outline: none;
    border: solid 2px #034427;
}
.container-items {
    display: flex;
    flex-wrap: wrap;
}
.items {
    max-width: 100px;
}
</style>
