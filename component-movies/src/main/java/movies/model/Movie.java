package movies.model;

import java.sql.Timestamp;

public class Movie {
    private int id;
    private Timestamp releaseDate;
    private String title;
    private int rating;
    private String author;
    private String format;

    public Movie(){}

    public Movie(int id,String title){
        this.id=id;
        this.title=title;
    }

    public Movie(int id,String title,String author){
        this(id,title);
        this.author=author;
    }

    public Movie(int id,String title,String author,int rating){
        this(id,title,author);
        this.rating=rating;
    }

    public Movie(int id,String title,String author,int rating,String format){
        this(id,title,author,rating);
        this.format=format;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Timestamp getReleaseDate() {
        return releaseDate;
    }

    public void setReleaseDate(Timestamp releaseDate) {
        this.releaseDate = releaseDate;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
}
