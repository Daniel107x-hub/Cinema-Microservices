package movies.service;

import movies.model.Movie;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class MovieService {

    public List<Movie> getAllMovies(){
        List<Movie> moviesList=new ArrayList<Movie>();
        moviesList.add(new Movie(0,"Harry potter","JK Rowling"));
        moviesList.add(new Movie(1,"The lord of the rings"));
        return moviesList;
    }

    public Movie getMovie(int id){
        return new Movie(id,"The lord of the rings "+id);
    }

}
