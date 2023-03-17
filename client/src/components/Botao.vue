<template>
    <div>
        <button type="submit">{{texto}}</button>
    </div>
</template>

<script>
export default {
    props: {
        texto: String
    }
}

</script>

<style scoped>
button[type="submit"] {
    padding: 10px;
    font-size: 18px;
    background-color: rgb(189, 100, 237);
    color: white;
    border: 3px solid black;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    box-sizing: border-box;
    min-width: 100px;
    justify-content: center;
}
</style>